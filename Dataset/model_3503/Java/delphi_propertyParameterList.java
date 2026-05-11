





import java.util.List;
import java.util.ArrayList;

public class delphi_propertyParameterList extends CSTrace {






    private List<delphi_typeId> delphi_typeids;




    private List<delphi_identList> delphi_identlists;


    public delphi_propertyParameterList(
    ) {
        super(
        );
        this.delphi_typeids = new ArrayList<>();
        this.delphi_identlists = new ArrayList<>();
    }

    public delphi_propertyParameterList(
        ArrayList<delphi_typeId> delphi_typeids,        ArrayList<delphi_identList> delphi_identlists    ) {
        this.delphi_typeids = delphi_typeids;
        this.delphi_identlists = delphi_identlists;
    }


    public List<delphi_typeId> getDelphi_typeids() {
        return delphi_typeids;
    }

    public void addDelphi_typeid(Delphi_typeid delphi_typeid) {
        this.delphi_typeids.add(delphi_typeid);
    }
    public List<delphi_identList> getDelphi_identlists() {
        return delphi_identlists;
    }

    public void addDelphi_identlist(Delphi_identlist delphi_identlist) {
        this.delphi_identlists.add(delphi_identlist);
    }

}