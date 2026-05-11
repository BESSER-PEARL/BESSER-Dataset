





import java.util.List;
import java.util.ArrayList;

public class remes_Constant extends Referable {

    private String type;
    private String value;
    private boolean global_;





    private remes_Mode remes_mode;




    private remes_Mode remes_mode;


    public remes_Constant(
        String type,        String value,        boolean global_    ) {
        super(
        );
        this.type = type;
        this.value = value;
        this.global_ = global_;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public boolean getGlobal_() {
        return global_;
    }

    public void setGlobal_(boolean global_) {
        this.global_ = global_;
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