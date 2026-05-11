





import java.util.List;
import java.util.ArrayList;

public class sql_ScalarOperand extends OperandList, RowValue {

    private String sostr;
    private String soint;
    private String sodate;
    private String soUInt;
    private String sotime;
    private String sodbl;
    private String sodt;



    public sql_ScalarOperand(
        String sostr,        String soint,        String sodate,        String soUInt,        String sotime,        String sodbl,        String sodt    ) {
        super(
        );
        this.sostr = sostr;
        this.soint = soint;
        this.sodate = sodate;
        this.soUInt = soUInt;
        this.sotime = sotime;
        this.sodbl = sodbl;
        this.sodt = sodt;
    }


    public String getSostr() {
        return sostr;
    }

    public void setSostr(String sostr) {
        this.sostr = sostr;
    }
    public String getSoint() {
        return soint;
    }

    public void setSoint(String soint) {
        this.soint = soint;
    }
    public String getSodate() {
        return sodate;
    }

    public void setSodate(String sodate) {
        this.sodate = sodate;
    }
    public String getSouint() {
        return soUInt;
    }

    public void setSouint(String soUInt) {
        this.soUInt = soUInt;
    }
    public String getSotime() {
        return sotime;
    }

    public void setSotime(String sotime) {
        this.sotime = sotime;
    }
    public String getSodbl() {
        return sodbl;
    }

    public void setSodbl(String sodbl) {
        this.sodbl = sodbl;
    }
    public String getSodt() {
        return sodt;
    }

    public void setSodt(String sodt) {
        this.sodt = sodt;
    }


}