




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_Promotion  {

    private String code;
    private LocalDate validTo;
    private LocalDate expirationDate;
    private String description;
    private LocalDate validFrom;
    private String roomType;
    private String percentage;



    public model_Promotion(
        String code,        LocalDate validTo,        LocalDate expirationDate,        String description,        LocalDate validFrom,        String roomType,        String percentage    ) {
        this.code = code;
        this.validTo = validTo;
        this.expirationDate = expirationDate;
        this.description = description;
        this.validFrom = validFrom;
        this.roomType = roomType;
        this.percentage = percentage;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public LocalDate getValidto() {
        return validTo;
    }

    public void setValidto(LocalDate validTo) {
        this.validTo = validTo;
    }
    public LocalDate getExpirationdate() {
        return expirationDate;
    }

    public void setExpirationdate(LocalDate expirationDate) {
        this.expirationDate = expirationDate;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public LocalDate getValidfrom() {
        return validFrom;
    }

    public void setValidfrom(LocalDate validFrom) {
        this.validFrom = validFrom;
    }
    public String getRoomtype() {
        return roomType;
    }

    public void setRoomtype(String roomType) {
        this.roomType = roomType;
    }
    public String getPercentage() {
        return percentage;
    }

    public void setPercentage(String percentage) {
        this.percentage = percentage;
    }


}