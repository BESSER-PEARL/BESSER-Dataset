





import java.util.List;
import java.util.ArrayList;

public class alldatatypes_Integers extends Type {

    private int int_01_EmptyDefault;
    private int int_01;
    private int hiddenInt_01;
    private int int_1;
    private int notEditableInt_01;
    private int ints;



    public alldatatypes_Integers(
        int int_01_EmptyDefault,        int int_01,        int hiddenInt_01,        int int_1,        int notEditableInt_01,        int ints    ) {
        super(
        );
        this.int_01_EmptyDefault = int_01_EmptyDefault;
        this.int_01 = int_01;
        this.hiddenInt_01 = hiddenInt_01;
        this.int_1 = int_1;
        this.notEditableInt_01 = notEditableInt_01;
        this.ints = ints;
    }


    public int getInt_01_emptydefault() {
        return int_01_EmptyDefault;
    }

    public void setInt_01_emptydefault(int int_01_EmptyDefault) {
        this.int_01_EmptyDefault = int_01_EmptyDefault;
    }
    public int getInt_01() {
        return int_01;
    }

    public void setInt_01(int int_01) {
        this.int_01 = int_01;
    }
    public int getHiddenint_01() {
        return hiddenInt_01;
    }

    public void setHiddenint_01(int hiddenInt_01) {
        this.hiddenInt_01 = hiddenInt_01;
    }
    public int getInt_1() {
        return int_1;
    }

    public void setInt_1(int int_1) {
        this.int_1 = int_1;
    }
    public int getNoteditableint_01() {
        return notEditableInt_01;
    }

    public void setNoteditableint_01(int notEditableInt_01) {
        this.notEditableInt_01 = notEditableInt_01;
    }
    public int getInts() {
        return ints;
    }

    public void setInts(int ints) {
        this.ints = ints;
    }


}