





import java.util.List;
import java.util.ArrayList;

public class codetaginfo_CodeTagInfo  {

    private String group;
    private String filename;





    private List<codetaginfo_CodeTag> codetaginfo_codetags;


    public codetaginfo_CodeTagInfo(
        String group,        String filename    ) {
        this.group = group;
        this.filename = filename;
        this.codetaginfo_codetags = new ArrayList<>();
    }

    public codetaginfo_CodeTagInfo(
        String group,        String filename        ArrayList<codetaginfo_CodeTag> codetaginfo_codetags    ) {
        this.group = group;
        this.filename = filename;
        this.codetaginfo_codetags = codetaginfo_codetags;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getFilename() {
        return filename;
    }

    public void setFilename(String filename) {
        this.filename = filename;
    }

    public List<codetaginfo_CodeTag> getCodetaginfo_codetags() {
        return codetaginfo_codetags;
    }

    public void addCodetaginfo_codetag(Codetaginfo_codetag codetaginfo_codetag) {
        this.codetaginfo_codetags.add(codetaginfo_codetag);
    }

}