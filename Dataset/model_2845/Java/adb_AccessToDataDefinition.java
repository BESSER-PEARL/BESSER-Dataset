





import java.util.List;
import java.util.ArrayList;

public class adb_AccessToDataDefinition extends AccessSpecification {

    private String generalAccessModifier;





    private adb_SubtypeIndication adb_subtypeindication;


    public adb_AccessToDataDefinition(
        String generalAccessModifier    ) {
        super(
        );
        this.generalAccessModifier = generalAccessModifier;
    }


    public String getGeneralaccessmodifier() {
        return generalAccessModifier;
    }

    public void setGeneralaccessmodifier(String generalAccessModifier) {
        this.generalAccessModifier = generalAccessModifier;
    }

    public adb_SubtypeIndication getAdb_subtypeindication() {
        return adb_subtypeindication;
    }

    public void setAdb_subtypeindication(adb_SubtypeIndication adb_subtypeindication) {
        this.adb_subtypeindication = adb_subtypeindication;
    }

}