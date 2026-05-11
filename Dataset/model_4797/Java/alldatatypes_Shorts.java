





import java.util.List;
import java.util.ArrayList;

public class alldatatypes_Shorts extends Type {

    private String short_01;
    private String notEditableShort_01;
    private String short_1;
    private String short_01_EmptyDefault;



    public alldatatypes_Shorts(
        String short_01,        String notEditableShort_01,        String short_1,        String short_01_EmptyDefault    ) {
        super(
        );
        this.short_01 = short_01;
        this.notEditableShort_01 = notEditableShort_01;
        this.short_1 = short_1;
        this.short_01_EmptyDefault = short_01_EmptyDefault;
    }


    public String getShort_01() {
        return short_01;
    }

    public void setShort_01(String short_01) {
        this.short_01 = short_01;
    }
    public String getNoteditableshort_01() {
        return notEditableShort_01;
    }

    public void setNoteditableshort_01(String notEditableShort_01) {
        this.notEditableShort_01 = notEditableShort_01;
    }
    public String getShort_1() {
        return short_1;
    }

    public void setShort_1(String short_1) {
        this.short_1 = short_1;
    }
    public String getShort_01_emptydefault() {
        return short_01_EmptyDefault;
    }

    public void setShort_01_emptydefault(String short_01_EmptyDefault) {
        this.short_01_EmptyDefault = short_01_EmptyDefault;
    }


}