





import java.util.List;
import java.util.ArrayList;

public class remes_Variable extends Referable {

    private boolean readable;
    private String type;
    private int vectorSize;
    private String value;
    private boolean writable;
    private boolean global_;





    private remes_Mode remes_mode;




    private remes_Mode remes_mode;


    public remes_Variable(
        boolean readable,        String type,        int vectorSize,        String value,        boolean writable,        boolean global_    ) {
        super(
        );
        this.readable = readable;
        this.type = type;
        this.vectorSize = vectorSize;
        this.value = value;
        this.writable = writable;
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
    public boolean getWritable() {
        return writable;
    }

    public void setWritable(boolean writable) {
        this.writable = writable;
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