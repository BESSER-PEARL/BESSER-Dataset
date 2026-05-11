





import java.util.List;
import java.util.ArrayList;

public class myDsl_enumeration_constant  {

    private String identifier;





    private myDsl_enumerator mydsl_enumerator;


    public myDsl_enumeration_constant(
        String identifier    ) {
        this.identifier = identifier;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public myDsl_enumerator getMydsl_enumerator() {
        return mydsl_enumerator;
    }

    public void setMydsl_enumerator(myDsl_enumerator mydsl_enumerator) {
        this.mydsl_enumerator = mydsl_enumerator;
    }

}