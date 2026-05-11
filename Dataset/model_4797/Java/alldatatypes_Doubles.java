





import java.util.List;
import java.util.ArrayList;

public class alldatatypes_Doubles extends Type {

    private float double_01;
    private float double_1;
    private float notEditableDouble_01;
    private float double_01_EmptyDefault;



    public alldatatypes_Doubles(
        float double_01,        float double_1,        float notEditableDouble_01,        float double_01_EmptyDefault    ) {
        super(
        );
        this.double_01 = double_01;
        this.double_1 = double_1;
        this.notEditableDouble_01 = notEditableDouble_01;
        this.double_01_EmptyDefault = double_01_EmptyDefault;
    }


    public float getDouble_01() {
        return double_01;
    }

    public void setDouble_01(float double_01) {
        this.double_01 = double_01;
    }
    public float getDouble_1() {
        return double_1;
    }

    public void setDouble_1(float double_1) {
        this.double_1 = double_1;
    }
    public float getNoteditabledouble_01() {
        return notEditableDouble_01;
    }

    public void setNoteditabledouble_01(float notEditableDouble_01) {
        this.notEditableDouble_01 = notEditableDouble_01;
    }
    public float getDouble_01_emptydefault() {
        return double_01_EmptyDefault;
    }

    public void setDouble_01_emptydefault(float double_01_EmptyDefault) {
        this.double_01_EmptyDefault = double_01_EmptyDefault;
    }


}