





import java.util.List;
import java.util.ArrayList;

public class sql_ScalarOperand extends OperandList, RowValue {

    private String sodbl;
    private String sotime;
    private String soUInt;
    private String sodt;
    private String sodate;
    private String soint;
    private String sostr;



    public sql_ScalarOperand(
        String sodbl,        String sotime,        String soUInt,        String sodt,        String sodate,        String soint,        String sostr    ) {
        super(
        );
        this.sodbl = sodbl;
        this.sotime = sotime;
        this.soUInt = soUInt;
        this.sodt = sodt;
        this.sodate = sodate;
        this.soint = soint;
        this.sostr = sostr;
    }


    public String getSodbl() {
        return sodbl;
    }

    public void setSodbl(String sodbl) {
        this.sodbl = sodbl;
    }
    public String getSotime() {
        return sotime;
    }

    public void setSotime(String sotime) {
        this.sotime = sotime;
    }
    public String getSouint() {
        return soUInt;
    }

    public void setSouint(String soUInt) {
        this.soUInt = soUInt;
    }
    public String getSodt() {
        return sodt;
    }

    public void setSodt(String sodt) {
        this.sodt = sodt;
    }
    public String getSodate() {
        return sodate;
    }

    public void setSodate(String sodate) {
        this.sodate = sodate;
    }
    public String getSoint() {
        return soint;
    }

    public void setSoint(String soint) {
        this.soint = soint;
    }
    public String getSostr() {
        return sostr;
    }

    public void setSostr(String sostr) {
        this.sostr = sostr;
    }


}