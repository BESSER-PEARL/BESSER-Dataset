





import java.util.List;
import java.util.ArrayList;

public class alldatatypes_Enums extends Type {

    private String states;
    private String enum_01;
    private String enums;
    private String heavy;
    private String notEditableEnum_01;
    private String statesMin1Max2;
    private String enum_1;
    private String statesMax2;
    private String enum_01_EmptyDefault;



    public alldatatypes_Enums(
        String states,        String enum_01,        String enums,        String heavy,        String notEditableEnum_01,        String statesMin1Max2,        String enum_1,        String statesMax2,        String enum_01_EmptyDefault    ) {
        super(
        );
        this.states = states;
        this.enum_01 = enum_01;
        this.enums = enums;
        this.heavy = heavy;
        this.notEditableEnum_01 = notEditableEnum_01;
        this.statesMin1Max2 = statesMin1Max2;
        this.enum_1 = enum_1;
        this.statesMax2 = statesMax2;
        this.enum_01_EmptyDefault = enum_01_EmptyDefault;
    }


    public String getStates() {
        return states;
    }

    public void setStates(String states) {
        this.states = states;
    }
    public String getEnum_01() {
        return enum_01;
    }

    public void setEnum_01(String enum_01) {
        this.enum_01 = enum_01;
    }
    public String getEnums() {
        return enums;
    }

    public void setEnums(String enums) {
        this.enums = enums;
    }
    public String getHeavy() {
        return heavy;
    }

    public void setHeavy(String heavy) {
        this.heavy = heavy;
    }
    public String getNoteditableenum_01() {
        return notEditableEnum_01;
    }

    public void setNoteditableenum_01(String notEditableEnum_01) {
        this.notEditableEnum_01 = notEditableEnum_01;
    }
    public String getStatesmin1max2() {
        return statesMin1Max2;
    }

    public void setStatesmin1max2(String statesMin1Max2) {
        this.statesMin1Max2 = statesMin1Max2;
    }
    public String getEnum_1() {
        return enum_1;
    }

    public void setEnum_1(String enum_1) {
        this.enum_1 = enum_1;
    }
    public String getStatesmax2() {
        return statesMax2;
    }

    public void setStatesmax2(String statesMax2) {
        this.statesMax2 = statesMax2;
    }
    public String getEnum_01_emptydefault() {
        return enum_01_EmptyDefault;
    }

    public void setEnum_01_emptydefault(String enum_01_EmptyDefault) {
        this.enum_01_EmptyDefault = enum_01_EmptyDefault;
    }


}