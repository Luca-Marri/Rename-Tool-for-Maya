import maya.cmds as cm



def rename_selected_meshes(new_name,padding):
    if not new_name:
        cm.warning("Insert a valid name")
        return

    meshes = cm.ls(selection=True, type="transform")


    if not meshes:
        cm.warning("No mesh selected")
        return

    numPadding = "0" * padding

    for i, mesh in enumerate(meshes, start=1):
        if padding == 0:
            cm.rename(mesh, f"{new_name}")
        else:
            try:
                cm.rename(mesh, f"{new_name}_{numPadding}{i}")
                print("== other")
            except Exception as e:
                cm.warning(f"Failed to rename {mesh}: {str(e)}")


def add_suffix(new_suff,LE_Text,isTrue):
    meshNames = cm.ls(selection=True, type="transform")

    for meshName in meshNames:
        new_name = f"{meshName}{LE_Text}{new_suff}" if isTrue else f"{meshName}{new_suff}{LE_Text}"
        cm.rename(meshName, new_name)

def add_prefix(new_pref,LE_Text,isTrue):
    meshNames = cm.ls(selection=True, type="transform")

    for meshName in meshNames:
        new_name = f"{new_pref}{LE_Text}{meshName}" if isTrue else f"{LE_Text}{new_pref}{meshName}"
        cm.rename(meshName, new_name)


def remove_characters(num_rmv, isFirst):
    meshNames = cm.ls(selection=True, type="transform")

    if not meshNames:
        cm.warning("No mesh selected, please select at least one mesh")

    for meshName in meshNames:
        if num_rmv >= len(meshName):
            cm.warning(f"Cannot remove {num_rmv} characters as the mesh name has only {len(meshName)} characters.")
            continue
        new_name = meshName[num_rmv:] if isFirst else meshName[:-num_rmv]
        cm.rename(meshName, new_name)


def slc_text(slc_text):

    selected_meshes = []

    if slc_text == "":
        cm.warning("No text inserted in Selected box")
        return

    meshNames = cm.ls(type="transform")
    selected_meshes = [mesh for mesh in meshNames if slc_text in mesh]
    if selected_meshes:
        cm.select(selected_meshes, replace=True)
    else:
        cm.warning(f"No Object named {slc_text}")


def Rpl_text(select_text, replace_text):

    if replace_text == "" or select_text == "":
        cm.warning("No text inserted")
        return

    meshNames = cm.ls(selection=True,type="transform")

    for meshName in meshNames:
        if select_text in meshName:
            new_name = meshName.replace(select_text, replace_text)
            cm.rename(meshName, new_name)



