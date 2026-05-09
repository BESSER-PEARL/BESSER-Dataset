





import java.util.List;
import java.util.ArrayList;

public class rif11a_ExchangeFile_SpecGroup extends SpecElementWithUserDefinedAttributes {






    private List<ExchangeFile_SpecObject> exchangefile_specobjects;


    public rif11a_ExchangeFile_SpecGroup(
    ) {
        super(
        );
        this.exchangefile_specobjects = new ArrayList<>();
    }

    public rif11a_ExchangeFile_SpecGroup(
        ArrayList<ExchangeFile_SpecObject> exchangefile_specobjects    ) {
        this.exchangefile_specobjects = exchangefile_specobjects;
    }


    public List<ExchangeFile_SpecObject> getExchangefile_specobjects() {
        return exchangefile_specobjects;
    }

    public void addExchangefile_specobject(Exchangefile_specobject exchangefile_specobject) {
        this.exchangefile_specobjects.add(exchangefile_specobject);
    }

}