





import java.util.List;
import java.util.ArrayList;

public class remes_Variable extends Referable {

    private boolean readable;
    private boolean global_;
    private String type;
    private boolean writable;
    private int vectorSize;
    private String value;





    private remes_Mode remes_mode;




    private remes_Mode remes_mode;


    public remes_Variable(
        boolean readable,        boolean global_,        String type,        boolean writable,        int vectorSize,        String value    ) {
        super(
        );
        this.readable = readable;
        this.global_ = global_;
        this.type = type;
        this.writable = writable;
        this.vectorSize = vectorSize;
        this.value = value;
    }


    public boolean getReadable() {
        return readable;
    }

    public void setReadable(boolean readable) {
        this.readable = readable;
    }
    public boolean getGlobal_() {
        return global_;
    }

    public void setGlobal_(boolean global_) {
        this.global_ = global_;
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
    public int getVectorsize() {
        return vectorSize;
    }

    public void setVectorsize(int vectorSize) {
        this.vectorSize = vectorSize;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
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