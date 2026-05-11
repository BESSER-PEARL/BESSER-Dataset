





import java.util.List;
import java.util.ArrayList;

public class alldatatypes_Floats extends Type {

    private float float_01;
    private float float_01_EmptyDefault;
    private float float_1;
    private float notEditableFloat_01;



    public alldatatypes_Floats(
        float float_01,        float float_01_EmptyDefault,        float float_1,        float notEditableFloat_01    ) {
        super(
        );
        this.float_01 = float_01;
        this.float_01_EmptyDefault = float_01_EmptyDefault;
        this.float_1 = float_1;
        this.notEditableFloat_01 = notEditableFloat_01;
    }


    public float getFloat_01() {
        return float_01;
    }

    public void setFloat_01(float float_01) {
        this.float_01 = float_01;
    }
    public float getFloat_01_emptydefault() {
        return float_01_EmptyDefault;
    }

    public void setFloat_01_emptydefault(float float_01_EmptyDefault) {
        this.float_01_EmptyDefault = float_01_EmptyDefault;
    }
    public float getFloat_1() {
        return float_1;
    }

    public void setFloat_1(float float_1) {
        this.float_1 = float_1;
    }
    public float getNoteditablefloat_01() {
        return notEditableFloat_01;
    }

    public void setNoteditablefloat_01(float notEditableFloat_01) {
        this.notEditableFloat_01 = notEditableFloat_01;
    }


}