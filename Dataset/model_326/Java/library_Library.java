





import java.util.List;
import java.util.ArrayList;

public class library_Library  {

    private String address;
    private int internalRequestCount;
    private int sumOfPages;
    private int requestCount;



    public library_Library(
        String address,        int internalRequestCount,        int sumOfPages,        int requestCount    ) {
        this.address = address;
        this.internalRequestCount = internalRequestCount;
        this.sumOfPages = sumOfPages;
        this.requestCount = requestCount;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getInternalrequestcount() {
        return internalRequestCount;
    }

    public void setInternalrequestcount(int internalRequestCount) {
        this.internalRequestCount = internalRequestCount;
    }
    public int getSumofpages() {
        return sumOfPages;
    }

    public void setSumofpages(int sumOfPages) {
        this.sumOfPages = sumOfPages;
    }
    public int getRequestcount() {
        return requestCount;
    }

    public void setRequestcount(int requestCount) {
        this.requestCount = requestCount;
    }


}