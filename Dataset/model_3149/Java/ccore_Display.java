





import java.util.List;
import java.util.ArrayList;

public class ccore_Display extends RuntimeItem {

    private boolean extendsUI;
    private boolean extendsIC;
    private boolean extendsMC;





    private ccore_Field ccore_field;


    public ccore_Display(
        boolean extendsUI,        boolean extendsIC,        boolean extendsMC    ) {
        super(
        );
        this.extendsUI = extendsUI;
        this.extendsIC = extendsIC;
        this.extendsMC = extendsMC;
    }


    public boolean getExtendsui() {
        return extendsUI;
    }

    public void setExtendsui(boolean extendsUI) {
        this.extendsUI = extendsUI;
    }
    public boolean getExtendsic() {
        return extendsIC;
    }

    public void setExtendsic(boolean extendsIC) {
        this.extendsIC = extendsIC;
    }
    public boolean getExtendsmc() {
        return extendsMC;
    }

    public void setExtendsmc(boolean extendsMC) {
        this.extendsMC = extendsMC;
    }

    public ccore_Field getCcore_field() {
        return ccore_field;
    }

    public void setCcore_field(ccore_Field ccore_field) {
        this.ccore_field = ccore_field;
    }

}