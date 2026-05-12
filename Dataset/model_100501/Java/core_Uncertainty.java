





import java.util.List;
import java.util.ArrayList;

public class core_Uncertainty extends IdentifiedElement {

    private String riskIndex;
    private String costsImpact;
    private String volatility;
    private String maturityIndex;
    private String scheduleImpact;
    private String precedence;
    private String propRiskIndex;





    private core_ContractualElement core_contractualelement;


    public core_Uncertainty(
        String riskIndex,        String costsImpact,        String volatility,        String maturityIndex,        String scheduleImpact,        String precedence,        String propRiskIndex    ) {
        super(
        );
        this.riskIndex = riskIndex;
        this.costsImpact = costsImpact;
        this.volatility = volatility;
        this.maturityIndex = maturityIndex;
        this.scheduleImpact = scheduleImpact;
        this.precedence = precedence;
        this.propRiskIndex = propRiskIndex;
    }


    public String getRiskindex() {
        return riskIndex;
    }

    public void setRiskindex(String riskIndex) {
        this.riskIndex = riskIndex;
    }
    public String getCostsimpact() {
        return costsImpact;
    }

    public void setCostsimpact(String costsImpact) {
        this.costsImpact = costsImpact;
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
    public String getScheduleimpact() {
        return scheduleImpact;
    }

    public void setScheduleimpact(String scheduleImpact) {
        this.scheduleImpact = scheduleImpact;
    }
    public String getPrecedence() {
        return precedence;
    }

    public void setPrecedence(String precedence) {
        this.precedence = precedence;
    }
    public String getPropriskindex() {
        return propRiskIndex;
    }

    public void setPropriskindex(String propRiskIndex) {
        this.propRiskIndex = propRiskIndex;
    }

    public core_ContractualElement getCore_contractualelement() {
        return core_contractualelement;
    }

    public void setCore_contractualelement(core_ContractualElement core_contractualelement) {
        this.core_contractualelement = core_contractualelement;
    }

}