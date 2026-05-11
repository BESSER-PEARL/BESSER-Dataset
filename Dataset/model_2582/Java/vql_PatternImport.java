





import java.util.List;
import java.util.ArrayList;

public class vql_PatternImport  {

    private String packageName;





    private vql_Pattern vql_pattern;




    private List<vql_Pattern> vql_patterns;




    private vql_VQLImportSection vql_vqlimportsection;


    public vql_PatternImport(
        String packageName    ) {
        this.packageName = packageName;
        this.vql_patterns = new ArrayList<>();
    }

    public vql_PatternImport(
        String packageName        ArrayList<vql_Pattern> vql_patterns    ) {
        this.packageName = packageName;
        this.vql_patterns = vql_patterns;
    }

    public String getPackagename() {
        return packageName;
    }

    public void setPackagename(String packageName) {
        this.packageName = packageName;
    }

    public vql_Pattern getVql_pattern() {
        return vql_pattern;
    }

    public void setVql_pattern(vql_Pattern vql_pattern) {
        this.vql_pattern = vql_pattern;
    }
    public List<vql_Pattern> getVql_patterns() {
        return vql_patterns;
    }

    public void addVql_pattern(Vql_pattern vql_pattern) {
        this.vql_patterns.add(vql_pattern);
    }
    public vql_VQLImportSection getVql_vqlimportsection() {
        return vql_vqlimportsection;
    }

    public void setVql_vqlimportsection(vql_VQLImportSection vql_vqlimportsection) {
        this.vql_vqlimportsection = vql_vqlimportsection;
    }

}