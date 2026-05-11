





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_DatetimeType extends BuiltInType {

    private int SecondPrecision_Max;
    private int SecondPrecision_Def;
    private int SecondPrecision_Min;
    private int YearPrecision_Min;
    private int YearPrecision_Max;
    private int DayPrecision_Min;
    private int DayPrecision_Def;
    private int DayPrecision_Max;
    private int YearPrecision_Def;
    private String Descriptor;



    public ORDB4ORA_DatetimeType(
        int SecondPrecision_Max,        int SecondPrecision_Def,        int SecondPrecision_Min,        int YearPrecision_Min,        int YearPrecision_Max,        int DayPrecision_Min,        int DayPrecision_Def,        int DayPrecision_Max,        int YearPrecision_Def,        String Descriptor    ) {
        super(
        );
        this.SecondPrecision_Max = SecondPrecision_Max;
        this.SecondPrecision_Def = SecondPrecision_Def;
        this.SecondPrecision_Min = SecondPrecision_Min;
        this.YearPrecision_Min = YearPrecision_Min;
        this.YearPrecision_Max = YearPrecision_Max;
        this.DayPrecision_Min = DayPrecision_Min;
        this.DayPrecision_Def = DayPrecision_Def;
        this.DayPrecision_Max = DayPrecision_Max;
        this.YearPrecision_Def = YearPrecision_Def;
        this.Descriptor = Descriptor;
    }


    public int getSecondprecision_max() {
        return SecondPrecision_Max;
    }

    public void setSecondprecision_max(int SecondPrecision_Max) {
        this.SecondPrecision_Max = SecondPrecision_Max;
    }
    public int getSecondprecision_def() {
        return SecondPrecision_Def;
    }

    public void setSecondprecision_def(int SecondPrecision_Def) {
        this.SecondPrecision_Def = SecondPrecision_Def;
    }
    public int getSecondprecision_min() {
        return SecondPrecision_Min;
    }

    public void setSecondprecision_min(int SecondPrecision_Min) {
        this.SecondPrecision_Min = SecondPrecision_Min;
    }
    public int getYearprecision_min() {
        return YearPrecision_Min;
    }

    public void setYearprecision_min(int YearPrecision_Min) {
        this.YearPrecision_Min = YearPrecision_Min;
    }
    public int getYearprecision_max() {
        return YearPrecision_Max;
    }

    public void setYearprecision_max(int YearPrecision_Max) {
        this.YearPrecision_Max = YearPrecision_Max;
    }
    public int getDayprecision_min() {
        return DayPrecision_Min;
    }

    public void setDayprecision_min(int DayPrecision_Min) {
        this.DayPrecision_Min = DayPrecision_Min;
    }
    public int getDayprecision_def() {
        return DayPrecision_Def;
    }

    public void setDayprecision_def(int DayPrecision_Def) {
        this.DayPrecision_Def = DayPrecision_Def;
    }
    public int getDayprecision_max() {
        return DayPrecision_Max;
    }

    public void setDayprecision_max(int DayPrecision_Max) {
        this.DayPrecision_Max = DayPrecision_Max;
    }
    public int getYearprecision_def() {
        return YearPrecision_Def;
    }

    public void setYearprecision_def(int YearPrecision_Def) {
        this.YearPrecision_Def = YearPrecision_Def;
    }
    public String getDescriptor() {
        return Descriptor;
    }

    public void setDescriptor(String Descriptor) {
        this.Descriptor = Descriptor;
    }


}