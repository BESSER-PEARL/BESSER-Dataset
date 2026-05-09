





import java.util.List;
import java.util.ArrayList;

public class cpntools_ColorSet extends Declaration {

    private String declare;
    private boolean timed;
    private String colorSetType;
    private String idname;





    private cpntools_Place cpntools_place;


    public cpntools_ColorSet(
        String declare,        boolean timed,        String colorSetType,        String idname    ) {
        super(
        );
        this.declare = declare;
        this.timed = timed;
        this.colorSetType = colorSetType;
        this.idname = idname;
    }


    public String getDeclare() {
        return declare;
    }

    public void setDeclare(String declare) {
        this.declare = declare;
    }
    public boolean getTimed() {
        return timed;
    }

    public void setTimed(boolean timed) {
        this.timed = timed;
    }
    public String getColorsettype() {
        return colorSetType;
    }

    public void setColorsettype(String colorSetType) {
        this.colorSetType = colorSetType;
    }
    public String getIdname() {
        return idname;
    }

    public void setIdname(String idname) {
        this.idname = idname;
    }

    public cpntools_Place getCpntools_place() {
        return cpntools_place;
    }

    public void setCpntools_place(cpntools_Place cpntools_place) {
        this.cpntools_place = cpntools_place;
    }

}