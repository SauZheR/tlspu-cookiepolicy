from Products.CMFCore.utils import getToolByName


def install(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if context.readDataFile('tlspu.cookiepolicy_install.txt') is None:
        return

    # Add additional setup code here


def uninstall(context):
    """Uninstall code.

    Note that CMFQuickInstaller removes some stuff for us
    automatically, though it is good form to remove it ourselves.  And
    it does not undo everything.  Most things that it does not handle,
    can be handled in GenericSetup xml files with a remove='True'
    added, but this is not supported for all files.  In some files it
    even breaks.  We handle those cases here.
    """

    if context.readDataFile('tlspu.cookiepolicy_uninstall.txt') is None:
        return

    portal = context.getSite()
    portal_conf = getToolByName(portal, 'portal_controlpanel')
    # Unregister our control panel configlet.
    portal_conf.unregisterConfiglet('cookiepolicy')

    # Remove our properties from portal properties.
    pp = getToolByName(portal, 'portal_properties')
    try:
        if hasattr(pp, 'tlspu_cookiepolicy_properties'):
            pp.manage_delObjects(ids='tlspu_cookiepolicy_properties')
    except KeyError:
        pass
