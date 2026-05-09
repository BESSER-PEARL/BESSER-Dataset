





import java.util.List;
import java.util.ArrayList;

public class UML2_OutputPin extends Pin {






    private UML2_CreateObjectAction uml2_createobjectaction;




    private UML2_ReadSelfAction uml2_readselfaction;


    public UML2_OutputPin(
    ) {
        super(
        );
    }



    public UML2_CreateObjectAction getUml2_createobjectaction() {
        return uml2_createobjectaction;
    }

    public void setUml2_createobjectaction(UML2_CreateObjectAction uml2_createobjectaction) {
        this.uml2_createobjectaction = uml2_createobjectaction;
    }
    public UML2_ReadSelfAction getUml2_readselfaction() {
        return uml2_readselfaction;
    }

    public void setUml2_readselfaction(UML2_ReadSelfAction uml2_readselfaction) {
        this.uml2_readselfaction = uml2_readselfaction;
    }

}