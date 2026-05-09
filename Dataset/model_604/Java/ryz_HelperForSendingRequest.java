





import java.util.List;
import java.util.ArrayList;

public class ryz_HelperForSendingRequest  {

    private String text;
    private String httpMethod;
    private String requestType;





    private List<ryz_UseCase> ryz_usecases;




    private ryz_PresentationElement ryz_presentationelement;




    private List<ryz_PresentationElement> ryz_presentationelements;




    private ryz_UseCase ryz_usecase;




    private ryz_AbstractView ryz_abstractview;


    public ryz_HelperForSendingRequest(
        String text,        String httpMethod,        String requestType    ) {
        this.text = text;
        this.httpMethod = httpMethod;
        this.requestType = requestType;
        this.ryz_usecases = new ArrayList<>();
        this.ryz_presentationelements = new ArrayList<>();
    }

    public ryz_HelperForSendingRequest(
        String text,        String httpMethod,        String requestType        ArrayList<ryz_UseCase> ryz_usecases,        ArrayList<ryz_PresentationElement> ryz_presentationelements    ) {
        this.text = text;
        this.httpMethod = httpMethod;
        this.requestType = requestType;
        this.ryz_usecases = ryz_usecases;
        this.ryz_presentationelements = ryz_presentationelements;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getHttpmethod() {
        return httpMethod;
    }

    public void setHttpmethod(String httpMethod) {
        this.httpMethod = httpMethod;
    }
    public String getRequesttype() {
        return requestType;
    }

    public void setRequesttype(String requestType) {
        this.requestType = requestType;
    }

    public List<ryz_UseCase> getRyz_usecases() {
        return ryz_usecases;
    }

    public void addRyz_usecase(Ryz_usecase ryz_usecase) {
        this.ryz_usecases.add(ryz_usecase);
    }
    public ryz_PresentationElement getRyz_presentationelement() {
        return ryz_presentationelement;
    }

    public void setRyz_presentationelement(ryz_PresentationElement ryz_presentationelement) {
        this.ryz_presentationelement = ryz_presentationelement;
    }
    public List<ryz_PresentationElement> getRyz_presentationelements() {
        return ryz_presentationelements;
    }

    public void addRyz_presentationelement(Ryz_presentationelement ryz_presentationelement) {
        this.ryz_presentationelements.add(ryz_presentationelement);
    }
    public ryz_UseCase getRyz_usecase() {
        return ryz_usecase;
    }

    public void setRyz_usecase(ryz_UseCase ryz_usecase) {
        this.ryz_usecase = ryz_usecase;
    }
    public ryz_AbstractView getRyz_abstractview() {
        return ryz_abstractview;
    }

    public void setRyz_abstractview(ryz_AbstractView ryz_abstractview) {
        this.ryz_abstractview = ryz_abstractview;
    }

}