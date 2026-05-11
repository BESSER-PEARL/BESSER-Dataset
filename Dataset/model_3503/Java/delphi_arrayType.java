





import java.util.List;
import java.util.ArrayList;

public class delphi_arrayType extends strucType {






    private delphi_type delphi_type;




    private List<delphi_ordinalType> delphi_ordinaltypes;




    private List<delphi_ordinalType> delphi_ordinaltypes;


    public delphi_arrayType(
    ) {
        super(
        );
        this.delphi_ordinaltypes = new ArrayList<>();
        this.delphi_ordinaltypes = new ArrayList<>();
    }

    public delphi_arrayType(
        ArrayList<delphi_ordinalType> delphi_ordinaltypes,        ArrayList<delphi_ordinalType> delphi_ordinaltypes    ) {
        this.delphi_ordinaltypes = delphi_ordinaltypes;
        this.delphi_ordinaltypes = delphi_ordinaltypes;
    }


    public delphi_type getDelphi_type() {
        return delphi_type;
    }

    public void setDelphi_type(delphi_type delphi_type) {
        this.delphi_type = delphi_type;
    }
    public List<delphi_ordinalType> getDelphi_ordinaltypes() {
        return delphi_ordinaltypes;
    }

    public void addDelphi_ordinaltype(Delphi_ordinaltype delphi_ordinaltype) {
        this.delphi_ordinaltypes.add(delphi_ordinaltype);
    }
    public List<delphi_ordinalType> getDelphi_ordinaltypes() {
        return delphi_ordinaltypes;
    }

    public void addDelphi_ordinaltype(Delphi_ordinaltype delphi_ordinaltype) {
        this.delphi_ordinaltypes.add(delphi_ordinaltype);
    }

}