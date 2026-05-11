





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_Varray extends Datatype {

    private int NumElements;
    private String Name;



    public ORDB4ORA_Varray(
        int NumElements,        String Name    ) {
        super(
        );
        this.NumElements = NumElements;
        this.Name = Name;
    }


    public int getNumelements() {
        return NumElements;
    }

    public void setNumelements(int NumElements) {
        this.NumElements = NumElements;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}