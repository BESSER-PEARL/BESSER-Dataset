





import java.util.List;
import java.util.ArrayList;

public class alldatatypes_BigIntegers extends Type {

    private String bigInts;
    private String bigInt_01;
    private String bigInt_1;
    private String bigInt_01_EmptyDefault;
    private String notEditableBigInt_01;



    public alldatatypes_BigIntegers(
        String bigInts,        String bigInt_01,        String bigInt_1,        String bigInt_01_EmptyDefault,        String notEditableBigInt_01    ) {
        super(
        );
        this.bigInts = bigInts;
        this.bigInt_01 = bigInt_01;
        this.bigInt_1 = bigInt_1;
        this.bigInt_01_EmptyDefault = bigInt_01_EmptyDefault;
        this.notEditableBigInt_01 = notEditableBigInt_01;
    }


    public String getBigints() {
        return bigInts;
    }

    public void setBigints(String bigInts) {
        this.bigInts = bigInts;
    }
    public String getBigint_01() {
        return bigInt_01;
    }

    public void setBigint_01(String bigInt_01) {
        this.bigInt_01 = bigInt_01;
    }
    public String getBigint_1() {
        return bigInt_1;
    }

    public void setBigint_1(String bigInt_1) {
        this.bigInt_1 = bigInt_1;
    }
    public String getBigint_01_emptydefault() {
        return bigInt_01_EmptyDefault;
    }

    public void setBigint_01_emptydefault(String bigInt_01_EmptyDefault) {
        this.bigInt_01_EmptyDefault = bigInt_01_EmptyDefault;
    }
    public String getNoteditablebigint_01() {
        return notEditableBigInt_01;
    }

    public void setNoteditablebigint_01(String notEditableBigInt_01) {
        this.notEditableBigInt_01 = notEditableBigInt_01;
    }


}