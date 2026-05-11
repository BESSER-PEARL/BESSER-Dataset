





import java.util.List;
import java.util.ArrayList;

public class myDsl01_Reference extends Property {

    private String multiplicity;





    private myDsl01_Reference mydsl01_reference;




    private myDsl01_Entity mydsl01_entity;


    public myDsl01_Reference(
        String multiplicity    ) {
        super(
        );
        this.multiplicity = multiplicity;
    }


    public String getMultiplicity() {
        return multiplicity;
    }

    public void setMultiplicity(String multiplicity) {
        this.multiplicity = multiplicity;
    }

    public myDsl01_Reference getMydsl01_reference() {
        return mydsl01_reference;
    }

    public void setMydsl01_reference(myDsl01_Reference mydsl01_reference) {
        this.mydsl01_reference = mydsl01_reference;
    }
    public myDsl01_Entity getMydsl01_entity() {
        return mydsl01_entity;
    }

    public void setMydsl01_entity(myDsl01_Entity mydsl01_entity) {
        this.mydsl01_entity = mydsl01_entity;
    }

}