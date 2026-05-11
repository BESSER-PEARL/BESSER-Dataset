





import java.util.List;
import java.util.ArrayList;

public class thingML_Reference extends Expression {






    private thingML_ElmtProperty thingml_elmtproperty;




    private thingML_ReferencedElmt thingml_referencedelmt;


    public thingML_Reference(
    ) {
        super(
        );
    }



    public thingML_ElmtProperty getThingml_elmtproperty() {
        return thingml_elmtproperty;
    }

    public void setThingml_elmtproperty(thingML_ElmtProperty thingml_elmtproperty) {
        this.thingml_elmtproperty = thingml_elmtproperty;
    }
    public thingML_ReferencedElmt getThingml_referencedelmt() {
        return thingml_referencedelmt;
    }

    public void setThingml_referencedelmt(thingML_ReferencedElmt thingml_referencedelmt) {
        this.thingml_referencedelmt = thingml_referencedelmt;
    }

}