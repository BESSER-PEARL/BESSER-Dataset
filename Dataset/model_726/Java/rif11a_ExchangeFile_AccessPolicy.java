





import java.util.List;
import java.util.ArrayList;

public class rif11a_ExchangeFile_AccessPolicy extends Identifiable {

    private String accessMode;





    private List<ExchangeFile_SpecObject> exchangefile_specobjects;




    private List<ExchangeFile_SpecHierarchy> exchangefile_spechierarchys;


    public rif11a_ExchangeFile_AccessPolicy(
        String accessMode    ) {
        super(
        );
        this.accessMode = accessMode;
        this.exchangefile_specobjects = new ArrayList<>();
        this.exchangefile_spechierarchys = new ArrayList<>();
    }

    public rif11a_ExchangeFile_AccessPolicy(
        String accessMode        ArrayList<ExchangeFile_SpecObject> exchangefile_specobjects,        ArrayList<ExchangeFile_SpecHierarchy> exchangefile_spechierarchys    ) {
        this.accessMode = accessMode;
        this.exchangefile_specobjects = exchangefile_specobjects;
        this.exchangefile_spechierarchys = exchangefile_spechierarchys;
    }

    public String getAccessmode() {
        return accessMode;
    }

    public void setAccessmode(String accessMode) {
        this.accessMode = accessMode;
    }

    public List<ExchangeFile_SpecObject> getExchangefile_specobjects() {
        return exchangefile_specobjects;
    }

    public void addExchangefile_specobject(Exchangefile_specobject exchangefile_specobject) {
        this.exchangefile_specobjects.add(exchangefile_specobject);
    }
    public List<ExchangeFile_SpecHierarchy> getExchangefile_spechierarchys() {
        return exchangefile_spechierarchys;
    }

    public void addExchangefile_spechierarchy(Exchangefile_spechierarchy exchangefile_spechierarchy) {
        this.exchangefile_spechierarchys.add(exchangefile_spechierarchy);
    }

}