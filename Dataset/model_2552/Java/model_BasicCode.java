





import java.util.List;
import java.util.ArrayList;

public class model_BasicCode  {

    private boolean structure;
    private String descriptions;
    private int sortHint;
    private String names;
    private String id;
    private boolean active;
    private int domain;





    private List<model_CodeEntry> model_codeentrys;




    private model_BasicCode model_basiccode;


    public model_BasicCode(
        boolean structure,        String descriptions,        int sortHint,        String names,        String id,        boolean active,        int domain    ) {
        this.structure = structure;
        this.descriptions = descriptions;
        this.sortHint = sortHint;
        this.names = names;
        this.id = id;
        this.active = active;
        this.domain = domain;
        this.model_codeentrys = new ArrayList<>();
    }

    public model_BasicCode(
        boolean structure,        String descriptions,        int sortHint,        String names,        String id,        boolean active,        int domain        ArrayList<model_CodeEntry> model_codeentrys    ) {
        this.structure = structure;
        this.descriptions = descriptions;
        this.sortHint = sortHint;
        this.names = names;
        this.id = id;
        this.active = active;
        this.domain = domain;
        this.model_codeentrys = model_codeentrys;
    }

    public boolean getStructure() {
        return structure;
    }

    public void setStructure(boolean structure) {
        this.structure = structure;
    }
    public String getDescriptions() {
        return descriptions;
    }

    public void setDescriptions(String descriptions) {
        this.descriptions = descriptions;
    }
    public int getSorthint() {
        return sortHint;
    }

    public void setSorthint(int sortHint) {
        this.sortHint = sortHint;
    }
    public String getNames() {
        return names;
    }

    public void setNames(String names) {
        this.names = names;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }
    public int getDomain() {
        return domain;
    }

    public void setDomain(int domain) {
        this.domain = domain;
    }

    public List<model_CodeEntry> getModel_codeentrys() {
        return model_codeentrys;
    }

    public void addModel_codeentry(Model_codeentry model_codeentry) {
        this.model_codeentrys.add(model_codeentry);
    }
    public model_BasicCode getModel_basiccode() {
        return model_basiccode;
    }

    public void setModel_basiccode(model_BasicCode model_basiccode) {
        this.model_basiccode = model_basiccode;
    }

}