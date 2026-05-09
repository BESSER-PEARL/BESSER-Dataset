





import java.util.List;
import java.util.ArrayList;

public class oaam_functions_ExternalTaskLink extends common_OaamBaseElementA, scenario_ModeDependentElementA, scenario_VariantDependentElementA {

    private String filter;



    public oaam_functions_ExternalTaskLink(
        String filter    ) {
        super(
        );
        this.filter = filter;
    }


    public String getFilter() {
        return filter;
    }

    public void setFilter(String filter) {
        this.filter = filter;
    }


}