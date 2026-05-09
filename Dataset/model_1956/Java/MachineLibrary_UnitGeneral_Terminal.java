





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_UnitGeneral_Terminal  {

    private String thisStation;
    private String station5;
    private String station3;
    private String station2;
    private String station1;
    private String station4;





    private MachineLibrary_UnitGeneralSpecial machinelibrary_unitgeneralspecial;


    public MachineLibrary_UnitGeneral_Terminal(
        String thisStation,        String station5,        String station3,        String station2,        String station1,        String station4    ) {
        this.thisStation = thisStation;
        this.station5 = station5;
        this.station3 = station3;
        this.station2 = station2;
        this.station1 = station1;
        this.station4 = station4;
    }


    public String getThisstation() {
        return thisStation;
    }

    public void setThisstation(String thisStation) {
        this.thisStation = thisStation;
    }
    public String getStation5() {
        return station5;
    }

    public void setStation5(String station5) {
        this.station5 = station5;
    }
    public String getStation3() {
        return station3;
    }

    public void setStation3(String station3) {
        this.station3 = station3;
    }
    public String getStation2() {
        return station2;
    }

    public void setStation2(String station2) {
        this.station2 = station2;
    }
    public String getStation1() {
        return station1;
    }

    public void setStation1(String station1) {
        this.station1 = station1;
    }
    public String getStation4() {
        return station4;
    }

    public void setStation4(String station4) {
        this.station4 = station4;
    }

    public MachineLibrary_UnitGeneralSpecial getMachinelibrary_unitgeneralspecial() {
        return machinelibrary_unitgeneralspecial;
    }

    public void setMachinelibrary_unitgeneralspecial(MachineLibrary_UnitGeneralSpecial machinelibrary_unitgeneralspecial) {
        this.machinelibrary_unitgeneralspecial = machinelibrary_unitgeneralspecial;
    }

}