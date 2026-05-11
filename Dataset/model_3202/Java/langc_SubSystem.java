





import java.util.List;
import java.util.ArrayList;

public class langc_SubSystem  {

    private String name;





    private List<langc_FolderName> langc_foldernames;




    private List<langc_FolderName> langc_foldernames;


    public langc_SubSystem(
        String name    ) {
        this.name = name;
        this.langc_foldernames = new ArrayList<>();
        this.langc_foldernames = new ArrayList<>();
    }

    public langc_SubSystem(
        String name        ArrayList<langc_FolderName> langc_foldernames,        ArrayList<langc_FolderName> langc_foldernames    ) {
        this.name = name;
        this.langc_foldernames = langc_foldernames;
        this.langc_foldernames = langc_foldernames;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<langc_FolderName> getLangc_foldernames() {
        return langc_foldernames;
    }

    public void addLangc_foldername(Langc_foldername langc_foldername) {
        this.langc_foldernames.add(langc_foldername);
    }
    public List<langc_FolderName> getLangc_foldernames() {
        return langc_foldernames;
    }

    public void addLangc_foldername(Langc_foldername langc_foldername) {
        this.langc_foldernames.add(langc_foldername);
    }

}