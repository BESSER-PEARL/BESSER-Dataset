





import java.util.List;
import java.util.ArrayList;

public class rdal_Uncertainty extends IdentifiedElement {

    private String costsImpact;
    private String propRiskIndex;
    private String riskIndex;
    private String maturityIndex;
    private String scheduleImpact;
    private String timeCriticality;
    private String familiarity;
    private String volatility;



    public rdal_Uncertainty(
        String costsImpact,        String propRiskIndex,        String riskIndex,        String maturityIndex,        String scheduleImpact,        String timeCriticality,        String familiarity,        String volatility    ) {
        super(
        );
        this.costsImpact = costsImpact;
        this.propRiskIndex = propRiskIndex;
        this.riskIndex = riskIndex;
        this.maturityIndex = maturityIndex;
        this.scheduleImpact = scheduleImpact;
        this.timeCriticality = timeCriticality;
        this.familiarity = familiarity;
        this.volatility = volatility;
    }


    public String getCostsimpact() {
        return costsImpact;
    }

    public void setCostsimpact(String costsImpact) {
        this.costsImpact = costsImpact;
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
    public String getTimecriticality() {
        return timeCriticality;
    }

    public void setTimecriticality(String timeCriticality) {
        this.timeCriticality = timeCriticality;
    }
    public String getFamiliarity() {
        return familiarity;
    }

    public void setFamiliarity(String familiarity) {
        this.familiarity = familiarity;
    }
    public String getVolatility() {
        return volatility;
    }

    public void setVolatility(String volatility) {
        this.volatility = volatility;
    }


}