





import java.util.List;
import java.util.ArrayList;

public class langc_System  {






    private List<langc_FolderName> langc_foldernames;




    private List<langc_SubSystem> langc_subsystems;


    public langc_System(
    ) {
        this.langc_foldernames = new ArrayList<>();
        this.langc_subsystems = new ArrayList<>();
    }

    public langc_System(
        ArrayList<langc_FolderName> langc_foldernames,        ArrayList<langc_SubSystem> langc_subsystems    ) {
        this.langc_foldernames = langc_foldernames;
        this.langc_subsystems = langc_subsystems;
    }


    public List<langc_FolderName> getLangc_foldernames() {
        return langc_foldernames;
    }

    public void addLangc_foldername(Langc_foldername langc_foldername) {
        this.langc_foldernames.add(langc_foldername);
    }
    public List<langc_SubSystem> getLangc_subsystems() {
        return langc_subsystems;
    }

    public void addLangc_subsystem(Langc_subsystem langc_subsystem) {
        this.langc_subsystems.add(langc_subsystem);
    }

}