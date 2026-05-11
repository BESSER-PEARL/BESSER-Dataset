





import java.util.List;
import java.util.ArrayList;

public class remes_Constant extends Referable {

    private boolean global_;
    private String value;
    private String type;





    private remes_Mode remes_mode;




    private remes_Mode remes_mode;


    public remes_Constant(
        boolean global_,        String value,        String type    ) {
        super(
        );
        this.global_ = global_;
        this.value = value;
        this.type = type;
    }


    public boolean getGlobal_() {
        return global_;
    }

    public void setGlobal_(boolean global_) {
        this.global_ = global_;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public remes_Mode getRemes_mode() {
        return remes_mode;
    }

    public void setRemes_mode(remes_Mode remes_mode) {
        this.remes_mode = remes_mode;
    }
    public remes_Mode getRemes_mode() {
        return remes_mode;
    }

    public void setRemes_mode(remes_Mode remes_mode) {
        this.remes_mode = remes_mode;
    }

}