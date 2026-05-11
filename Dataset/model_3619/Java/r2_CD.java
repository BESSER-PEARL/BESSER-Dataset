





import java.util.List;
import java.util.ArrayList;

public class r2_CD extends ANY {

    private String codeSystemName;
    private String valueSet;
    private String codeSystemVersion;
    private String valueSetVersion;
    private String code;
    private String codeSystem;





    private List<r2_CD> r2_cds;


    public r2_CD(
        String codeSystemName,        String valueSet,        String codeSystemVersion,        String valueSetVersion,        String code,        String codeSystem    ) {
        super(
        );
        this.codeSystemName = codeSystemName;
        this.valueSet = valueSet;
        this.codeSystemVersion = codeSystemVersion;
        this.valueSetVersion = valueSetVersion;
        this.code = code;
        this.codeSystem = codeSystem;
        this.r2_cds = new ArrayList<>();
    }

    public r2_CD(
        String codeSystemName,        String valueSet,        String codeSystemVersion,        String valueSetVersion,        String code,        String codeSystem        ArrayList<r2_CD> r2_cds    ) {
        this.codeSystemName = codeSystemName;
        this.valueSet = valueSet;
        this.codeSystemVersion = codeSystemVersion;
        this.valueSetVersion = valueSetVersion;
        this.code = code;
        this.codeSystem = codeSystem;
        this.r2_cds = r2_cds;
    }

    public String getCodesystemname() {
        return codeSystemName;
    }

    public void setCodesystemname(String codeSystemName) {
        this.codeSystemName = codeSystemName;
    }
    public String getValueset() {
        return valueSet;
    }

    public void setValueset(String valueSet) {
        this.valueSet = valueSet;
    }
    public String getCodesystemversion() {
        return codeSystemVersion;
    }

    public void setCodesystemversion(String codeSystemVersion) {
        this.codeSystemVersion = codeSystemVersion;
    }
    public String getValuesetversion() {
        return valueSetVersion;
    }

    public void setValuesetversion(String valueSetVersion) {
        this.valueSetVersion = valueSetVersion;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getCodesystem() {
        return codeSystem;
    }

    public void setCodesystem(String codeSystem) {
        this.codeSystem = codeSystem;
    }

    public List<r2_CD> getR2_cds() {
        return r2_cds;
    }

    public void addR2_cd(R2_cd r2_cd) {
        this.r2_cds.add(r2_cd);
    }

}