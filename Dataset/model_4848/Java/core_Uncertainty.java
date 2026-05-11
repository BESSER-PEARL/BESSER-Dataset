





import java.util.List;
import java.util.ArrayList;

public class core_Uncertainty extends IdentifiedElement {

    private String propRiskIndex;
    private String scheduleImpact;
    private String costsImpact;
    private String precedence;
    private String maturityIndex;
    private String volatility;
    private String riskIndex;





    private core_ContractualElement core_contractualelement;


    public core_Uncertainty(
        String propRiskIndex,        String scheduleImpact,        String costsImpact,        String precedence,        String maturityIndex,        String volatility,        String riskIndex    ) {
        super(
        );
        this.propRiskIndex = propRiskIndex;
        this.scheduleImpact = scheduleImpact;
        this.costsImpact = costsImpact;
        this.precedence = precedence;
        this.maturityIndex = maturityIndex;
        this.volatility = volatility;
        this.riskIndex = riskIndex;
    }


    public String getPropriskindex() {
        return propRiskIndex;
    }

    public void setPropriskindex(String propRiskIndex) {
        this.propRiskIndex = propRiskIndex;
    }
    public String getScheduleimpact() {
        return scheduleImpact;
    }

    public void setScheduleimpact(String scheduleImpact) {
        this.scheduleImpact = scheduleImpact;
    }
    public String getCostsimpact() {
        return costsImpact;
    }

    public void setCostsimpact(String costsImpact) {
        this.costsImpact = costsImpact;
    }
    public String getPrecedence() {
        return precedence;
    }

    public void setPrecedence(String precedence) {
        this.precedence = precedence;
    }
    public String getMaturityindex() {
        return maturityIndex;
    }

    public void setMaturityindex(String maturityIndex) {
        this.maturityIndex = maturityIndex;
    }
    public String getVolatility() {
        return volatility;
    }

    public void setVolatility(String volatility) {
        this.volatility = volatility;
    }
    public String getRiskindex() {
        return riskIndex;
    }

    public void setRiskindex(String riskIndex) {
        this.riskIndex = riskIndex;
    }

    public core_ContractualElement getCore_contractualelement() {
        return core_contractualelement;
    }

    public void setCore_contractualelement(core_ContractualElement core_contractualelement) {
        this.core_contractualelement = core_contractualelement;
    }

}