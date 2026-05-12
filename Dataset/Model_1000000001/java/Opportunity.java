




import java.time.LocalDate;
import java.time.LocalDateTime;

import java.util.List;
import java.util.ArrayList;

public class Opportunity  {

    private int id;
    private None stage;
    private int probability;
    private LocalDateTime updated_at;
    private LocalDate expected_close_date;
    private String description;
    private LocalDateTime created_at;
    private String title;
    private float value;
    private LocalDateTime closed_at;



    public Opportunity(
        int id,        None stage,        int probability,        LocalDateTime updated_at,        LocalDate expected_close_date,        String description,        LocalDateTime created_at,        String title,        float value,        LocalDateTime closed_at    ) {
        this.id = id;
        this.stage = stage;
        this.probability = probability;
        this.updated_at = updated_at;
        this.expected_close_date = expected_close_date;
        this.description = description;
        this.created_at = created_at;
        this.title = title;
        this.value = value;
        this.closed_at = closed_at;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public None getStage() {
        return stage;
    }

    public void setStage(None stage) {
        this.stage = stage;
    }
    public int getProbability() {
        return probability;
    }

    public void setProbability(int probability) {
        this.probability = probability;
    }
    public LocalDateTime getUpdated_at() {
        return updated_at;
    }

    public void setUpdated_at(LocalDateTime updated_at) {
        this.updated_at = updated_at;
    }
    public LocalDate getExpected_close_date() {
        return expected_close_date;
    }

    public void setExpected_close_date(LocalDate expected_close_date) {
        this.expected_close_date = expected_close_date;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public LocalDateTime getCreated_at() {
        return created_at;
    }

    public void setCreated_at(LocalDateTime created_at) {
        this.created_at = created_at;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }
    public LocalDateTime getClosed_at() {
        return closed_at;
    }

    public void setClosed_at(LocalDateTime closed_at) {
        this.closed_at = closed_at;
    }


}