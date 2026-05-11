





import java.util.List;
import java.util.ArrayList;

public class muddle_MuddleElementType extends Type {






    private muddle_MuddleElement muddle_muddleelement;




    private List<muddle_MuddleElementType> muddle_muddleelementtypes;




    private List<muddle_MuddleElement> muddle_muddleelements;




    private List<muddle_MuddleElementType> muddle_muddleelementtypes;


    public muddle_MuddleElementType(
    ) {
        super(
        );
        this.muddle_muddleelementtypes = new ArrayList<>();
        this.muddle_muddleelements = new ArrayList<>();
        this.muddle_muddleelementtypes = new ArrayList<>();
    }

    public muddle_MuddleElementType(
        ArrayList<muddle_MuddleElementType> muddle_muddleelementtypes,        ArrayList<muddle_MuddleElement> muddle_muddleelements,        ArrayList<muddle_MuddleElementType> muddle_muddleelementtypes    ) {
        this.muddle_muddleelementtypes = muddle_muddleelementtypes;
        this.muddle_muddleelements = muddle_muddleelements;
        this.muddle_muddleelementtypes = muddle_muddleelementtypes;
    }


    public muddle_MuddleElement getMuddle_muddleelement() {
        return muddle_muddleelement;
    }

    public void setMuddle_muddleelement(muddle_MuddleElement muddle_muddleelement) {
        this.muddle_muddleelement = muddle_muddleelement;
    }
    public List<muddle_MuddleElementType> getMuddle_muddleelementtypes() {
        return muddle_muddleelementtypes;
    }

    public void addMuddle_muddleelementtype(Muddle_muddleelementtype muddle_muddleelementtype) {
        this.muddle_muddleelementtypes.add(muddle_muddleelementtype);
    }
    public List<muddle_MuddleElement> getMuddle_muddleelements() {
        return muddle_muddleelements;
    }

    public void addMuddle_muddleelement(Muddle_muddleelement muddle_muddleelement) {
        this.muddle_muddleelements.add(muddle_muddleelement);
    }
    public List<muddle_MuddleElementType> getMuddle_muddleelementtypes() {
        return muddle_muddleelementtypes;
    }

    public void addMuddle_muddleelementtype(Muddle_muddleelementtype muddle_muddleelementtype) {
        this.muddle_muddleelementtypes.add(muddle_muddleelementtype);
    }

}