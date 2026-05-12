





import java.util.List;
import java.util.ArrayList;

public class core_Uncertainty extends IdentifiedElement {

    private String scheduleImpact;
    private String volatility;
    private String maturityIndex;
    private String propRiskIndex;
    private String riskIndex;
    private String precedence;
    private String costsImpact;





    private core_ContractualElement core_contractualelement;


    public core_Uncertainty(
        String scheduleImpact,        String volatility,        String maturityIndex,        String propRiskIndex,        String riskIndex,        String precedence,        String costsImpact    ) {
        super(
        );
        this.scheduleImpact = scheduleImpact;
        this.volatility = volatility;
        this.maturityIndex = maturityIndex;
        this.propRiskIndex = propRiskIndex;
        this.riskIndex = riskIndex;
        this.precedence = precedence;
        this.costsImpact = costsImpact;
    }


    public String getScheduleimpact() {
        return scheduleImpact;
    }

    public void setScheduleimpact(String scheduleImpact) {
        this.scheduleImpact = scheduleImpact;
    }
    public String getVolatility() {
        return volatility;
    }

    public void setVolatility(String volatility) {
        this.volatility = volatility;
    }
    public String getMaturityindex() {
        return maturityIndex;
    }

    public void setMaturityindex(String maturityIndex) {
        this.maturityIndex = maturityIndex;
    }
    public String getPropriskindex() {
        return propRiskIndex;
    }

    public void setPropriskindex(String propRiskIndex) {
        this.propRiskIndex = propRiskIndex;
    }
    public String getRiskindex() {
        return riskIndex;
    }

    public void setRiskindex(String riskIndex) {
        this.riskIndex = riskIndex;
    }
    public String getPrecedence() {
        return precedence;
    }

    public void setPrecedence(String precedence) {
        this.precedence = precedence;
    }
    public String getCostsimpact() {
        return costsImpact;
    }

    public void setCostsimpact(String costsImpact) {
        this.costsImpact = costsImpact;
    }

    public core_ContractualElement getCore_contractualelement() {
        return core_contractualelement;
    }

    public void setCore_contractualelement(core_ContractualElement core_contractualelement) {
        this.core_contractualelement = core_contractualelement;
    }

}