





import java.util.List;
import java.util.ArrayList;

public class remes_Variable extends Referable {

    private boolean global_;
    private boolean readable;
    private String type;
    private boolean writable;
    private String value;
    private int vectorSize;





    private remes_Mode remes_mode;




    private remes_Mode remes_mode;


    public remes_Variable(
        boolean global_,        boolean readable,        String type,        boolean writable,        String value,        int vectorSize    ) {
        super(
        );
        this.global_ = global_;
        this.readable = readable;
        this.type = type;
        this.writable = writable;
        this.value = value;
        this.vectorSize = vectorSize;
    }


    public boolean getGlobal_() {
        return global_;
    }

    public void setGlobal_(boolean global_) {
        this.global_ = global_;
    }
    public boolean getReadable() {
        return readable;
    }

    public void setReadable(boolean readable) {
        this.readable = readable;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getWritable() {
        return writable;
    }

    public void setWritable(boolean writable) {
        this.writable = writable;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public int getVectorsize() {
        return vectorSize;
    }

    public void setVectorsize(int vectorSize) {
        this.vectorSize = vectorSize;
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