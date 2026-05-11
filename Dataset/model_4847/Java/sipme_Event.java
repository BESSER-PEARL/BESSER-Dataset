




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class sipme_Event extends SIPME_object {

    private String source;
    private String occurenceProbability;
    private String frequency;
    private LocalDate timeStamp;





    private sipme_EnterpriseProcessor sipme_enterpriseprocessor;




    private sipme_Event sipme_event;




    private sipme_EnterpriseProcessor sipme_enterpriseprocessor;




    private List<sipme_EnterpriseProcessor> sipme_enterpriseprocessors;




    private List<sipme_EnterpriseProcessor> sipme_enterpriseprocessors;


    public sipme_Event(
        String source,        String occurenceProbability,        String frequency,        LocalDate timeStamp    ) {
        super(
        );
        this.source = source;
        this.occurenceProbability = occurenceProbability;
        this.frequency = frequency;
        this.timeStamp = timeStamp;
        this.sipme_enterpriseprocessors = new ArrayList<>();
        this.sipme_enterpriseprocessors = new ArrayList<>();
    }

    public sipme_Event(
        String source,        String occurenceProbability,        String frequency,        LocalDate timeStamp        ArrayList<sipme_EnterpriseProcessor> sipme_enterpriseprocessors,        ArrayList<sipme_EnterpriseProcessor> sipme_enterpriseprocessors    ) {
        this.source = source;
        this.occurenceProbability = occurenceProbability;
        this.frequency = frequency;
        this.timeStamp = timeStamp;
        this.sipme_enterpriseprocessors = sipme_enterpriseprocessors;
        this.sipme_enterpriseprocessors = sipme_enterpriseprocessors;
    }

    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getOccurenceprobability() {
        return occurenceProbability;
    }

    public void setOccurenceprobability(String occurenceProbability) {
        this.occurenceProbability = occurenceProbability;
    }
    public String getFrequency() {
        return frequency;
    }

    public void setFrequency(String frequency) {
        this.frequency = frequency;
    }
    public LocalDate getTimestamp() {
        return timeStamp;
    }

    public void setTimestamp(LocalDate timeStamp) {
        this.timeStamp = timeStamp;
    }

    public sipme_EnterpriseProcessor getSipme_enterpriseprocessor() {
        return sipme_enterpriseprocessor;
    }

    public void setSipme_enterpriseprocessor(sipme_EnterpriseProcessor sipme_enterpriseprocessor) {
        this.sipme_enterpriseprocessor = sipme_enterpriseprocessor;
    }
    public sipme_Event getSipme_event() {
        return sipme_event;
    }

    public void setSipme_event(sipme_Event sipme_event) {
        this.sipme_event = sipme_event;
    }
    public sipme_EnterpriseProcessor getSipme_enterpriseprocessor() {
        return sipme_enterpriseprocessor;
    }

    public void setSipme_enterpriseprocessor(sipme_EnterpriseProcessor sipme_enterpriseprocessor) {
        this.sipme_enterpriseprocessor = sipme_enterpriseprocessor;
    }
    public List<sipme_EnterpriseProcessor> getSipme_enterpriseprocessors() {
        return sipme_enterpriseprocessors;
    }

    public void addSipme_enterpriseprocessor(Sipme_enterpriseprocessor sipme_enterpriseprocessor) {
        this.sipme_enterpriseprocessors.add(sipme_enterpriseprocessor);
    }
    public List<sipme_EnterpriseProcessor> getSipme_enterpriseprocessors() {
        return sipme_enterpriseprocessors;
    }

    public void addSipme_enterpriseprocessor(Sipme_enterpriseprocessor sipme_enterpriseprocessor) {
        this.sipme_enterpriseprocessors.add(sipme_enterpriseprocessor);
    }

}