





import java.util.List;
import java.util.ArrayList;

public class UML2_LinkEndData extends Element {






    private UML2_Property uml2_property;




    private UML2_InputPin uml2_inputpin;


    public UML2_LinkEndData(
    ) {
        super(
        );
    }



    public UML2_Property getUml2_property() {
        return uml2_property;
    }

    public void setUml2_property(UML2_Property uml2_property) {
        this.uml2_property = uml2_property;
    }
    public UML2_InputPin getUml2_inputpin() {
        return uml2_inputpin;
    }

    public void setUml2_inputpin(UML2_InputPin uml2_inputpin) {
        this.uml2_inputpin = uml2_inputpin;
    }

}