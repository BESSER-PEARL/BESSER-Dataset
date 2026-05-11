





import java.util.List;
import java.util.ArrayList;

public class oogen_OOVariable extends OOStatement {

    private boolean transient;
    private String name;





    private oogen_OOConstructor oogen_ooconstructor;




    private oogen_OOMethod oogen_oomethod;


    public oogen_OOVariable(
        boolean transient,        String name    ) {
        super(
        );
        this.transient = transient;
        this.name = name;
    }


    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public oogen_OOConstructor getOogen_ooconstructor() {
        return oogen_ooconstructor;
    }

    public void setOogen_ooconstructor(oogen_OOConstructor oogen_ooconstructor) {
        this.oogen_ooconstructor = oogen_ooconstructor;
    }
    public oogen_OOMethod getOogen_oomethod() {
        return oogen_oomethod;
    }

    public void setOogen_oomethod(oogen_OOMethod oogen_oomethod) {
        this.oogen_oomethod = oogen_oomethod;
    }

}