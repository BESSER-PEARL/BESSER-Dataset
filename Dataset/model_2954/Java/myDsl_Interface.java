





import java.util.List;
import java.util.ArrayList;

public class myDsl_Interface extends Type {






    private myDsl_Interface mydsl_interface;




    private List<myDsl_Attribute> mydsl_attributes;


    public myDsl_Interface(
    ) {
        super(
        );
        this.mydsl_attributes = new ArrayList<>();
    }

    public myDsl_Interface(
        ArrayList<myDsl_Attribute> mydsl_attributes    ) {
        this.mydsl_attributes = mydsl_attributes;
    }


    public myDsl_Interface getMydsl_interface() {
        return mydsl_interface;
    }

    public void setMydsl_interface(myDsl_Interface mydsl_interface) {
        this.mydsl_interface = mydsl_interface;
    }
    public List<myDsl_Attribute> getMydsl_attributes() {
        return mydsl_attributes;
    }

    public void addMydsl_attribute(Mydsl_attribute mydsl_attribute) {
        this.mydsl_attributes.add(mydsl_attribute);
    }

}