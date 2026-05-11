





import java.util.List;
import java.util.ArrayList;

public class alldatatypes_Longs extends Type {

    private String notEditableLong_01;
    private String long_01_EmptyDefault;
    private String long_01;
    private String long_1;



    public alldatatypes_Longs(
        String notEditableLong_01,        String long_01_EmptyDefault,        String long_01,        String long_1    ) {
        super(
        );
        this.notEditableLong_01 = notEditableLong_01;
        this.long_01_EmptyDefault = long_01_EmptyDefault;
        this.long_01 = long_01;
        this.long_1 = long_1;
    }


    public String getNoteditablelong_01() {
        return notEditableLong_01;
    }

    public void setNoteditablelong_01(String notEditableLong_01) {
        this.notEditableLong_01 = notEditableLong_01;
    }
    public String getLong_01_emptydefault() {
        return long_01_EmptyDefault;
    }

    public void setLong_01_emptydefault(String long_01_EmptyDefault) {
        this.long_01_EmptyDefault = long_01_EmptyDefault;
    }
    public String getLong_01() {
        return long_01;
    }

    public void setLong_01(String long_01) {
        this.long_01 = long_01;
    }
    public String getLong_1() {
        return long_1;
    }

    public void setLong_1(String long_1) {
        this.long_1 = long_1;
    }


}