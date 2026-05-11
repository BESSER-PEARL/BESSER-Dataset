





import java.util.List;
import java.util.ArrayList;

public class sipme_ObjectView extends SIPME_object {

    private String viewPoint;





    private sipme_EnterpriseProcessor sipme_enterpriseprocessor;




    private sipme_EnterpriseProcessor sipme_enterpriseprocessor;




    private List<sipme_Event> sipme_events;




    private sipme_EnterpriseObject sipme_enterpriseobject;




    private sipme_EnterpriseProcessor sipme_enterpriseprocessor;




    private sipme_EnterpriseObject sipme_enterpriseobject;




    private sipme_Event sipme_event;


    public sipme_ObjectView(
        String viewPoint    ) {
        super(
        );
        this.viewPoint = viewPoint;
        this.sipme_events = new ArrayList<>();
    }

    public sipme_ObjectView(
        String viewPoint        ArrayList<sipme_Event> sipme_events    ) {
        this.viewPoint = viewPoint;
        this.sipme_events = sipme_events;
    }

    public String getViewpoint() {
        return viewPoint;
    }

    public void setViewpoint(String viewPoint) {
        this.viewPoint = viewPoint;
    }

    public sipme_EnterpriseProcessor getSipme_enterpriseprocessor() {
        return sipme_enterpriseprocessor;
    }

    public void setSipme_enterpriseprocessor(sipme_EnterpriseProcessor sipme_enterpriseprocessor) {
        this.sipme_enterpriseprocessor = sipme_enterpriseprocessor;
    }
    public sipme_EnterpriseProcessor getSipme_enterpriseprocessor() {
        return sipme_enterpriseprocessor;
    }

    public void setSipme_enterpriseprocessor(sipme_EnterpriseProcessor sipme_enterpriseprocessor) {
        this.sipme_enterpriseprocessor = sipme_enterpriseprocessor;
    }
    public List<sipme_Event> getSipme_events() {
        return sipme_events;
    }

    public void addSipme_event(Sipme_event sipme_event) {
        this.sipme_events.add(sipme_event);
    }
    public sipme_EnterpriseObject getSipme_enterpriseobject() {
        return sipme_enterpriseobject;
    }

    public void setSipme_enterpriseobject(sipme_EnterpriseObject sipme_enterpriseobject) {
        this.sipme_enterpriseobject = sipme_enterpriseobject;
    }
    public sipme_EnterpriseProcessor getSipme_enterpriseprocessor() {
        return sipme_enterpriseprocessor;
    }

    public void setSipme_enterpriseprocessor(sipme_EnterpriseProcessor sipme_enterpriseprocessor) {
        this.sipme_enterpriseprocessor = sipme_enterpriseprocessor;
    }
    public sipme_EnterpriseObject getSipme_enterpriseobject() {
        return sipme_enterpriseobject;
    }

    public void setSipme_enterpriseobject(sipme_EnterpriseObject sipme_enterpriseobject) {
        this.sipme_enterpriseobject = sipme_enterpriseobject;
    }
    public sipme_Event getSipme_event() {
        return sipme_event;
    }

    public void setSipme_event(sipme_Event sipme_event) {
        this.sipme_event = sipme_event;
    }

}