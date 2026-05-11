





import java.util.List;
import java.util.ArrayList;

public class etrace_LinkType  {

    private String uses;
    private String example;
    private String purpose;
    private String name;
    private String description;





    private etrace_AbstractLink etrace_abstractlink;




    private List<etrace_LinkType> etrace_linktypes;




    private etrace_LinkType etrace_linktype;


    public etrace_LinkType(
        String uses,        String example,        String purpose,        String name,        String description    ) {
        this.uses = uses;
        this.example = example;
        this.purpose = purpose;
        this.name = name;
        this.description = description;
        this.etrace_linktypes = new ArrayList<>();
    }

    public etrace_LinkType(
        String uses,        String example,        String purpose,        String name,        String description        ArrayList<etrace_LinkType> etrace_linktypes    ) {
        this.uses = uses;
        this.example = example;
        this.purpose = purpose;
        this.name = name;
        this.description = description;
        this.etrace_linktypes = etrace_linktypes;
    }

    public String getUses() {
        return uses;
    }

    public void setUses(String uses) {
        this.uses = uses;
    }
    public String getExample() {
        return example;
    }

    public void setExample(String example) {
        this.example = example;
    }
    public String getPurpose() {
        return purpose;
    }

    public void setPurpose(String purpose) {
        this.purpose = purpose;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public etrace_AbstractLink getEtrace_abstractlink() {
        return etrace_abstractlink;
    }

    public void setEtrace_abstractlink(etrace_AbstractLink etrace_abstractlink) {
        this.etrace_abstractlink = etrace_abstractlink;
    }
    public List<etrace_LinkType> getEtrace_linktypes() {
        return etrace_linktypes;
    }

    public void addEtrace_linktype(Etrace_linktype etrace_linktype) {
        this.etrace_linktypes.add(etrace_linktype);
    }
    public etrace_LinkType getEtrace_linktype() {
        return etrace_linktype;
    }

    public void setEtrace_linktype(etrace_LinkType etrace_linktype) {
        this.etrace_linktype = etrace_linktype;
    }

}