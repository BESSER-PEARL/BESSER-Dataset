





import java.util.List;
import java.util.ArrayList;

public class MyMouseListener  {

    private boolean hasSelected;
    private boolean singleCardSelected;
    private boolean rightClicked;
    private String tempCard;
    private String clickedCard;
    private String source;
    private String temp;
    private String destination;



    public MyMouseListener(
        boolean hasSelected,        boolean singleCardSelected,        boolean rightClicked,        String tempCard,        String clickedCard,        String source,        String temp,        String destination    ) {
        this.hasSelected = hasSelected;
        this.singleCardSelected = singleCardSelected;
        this.rightClicked = rightClicked;
        this.tempCard = tempCard;
        this.clickedCard = clickedCard;
        this.source = source;
        this.temp = temp;
        this.destination = destination;
    }


    public boolean getHasselected() {
        return hasSelected;
    }

    public void setHasselected(boolean hasSelected) {
        this.hasSelected = hasSelected;
    }
    public boolean getSinglecardselected() {
        return singleCardSelected;
    }

    public void setSinglecardselected(boolean singleCardSelected) {
        this.singleCardSelected = singleCardSelected;
    }
    public boolean getRightclicked() {
        return rightClicked;
    }

    public void setRightclicked(boolean rightClicked) {
        this.rightClicked = rightClicked;
    }
    public String getTempcard() {
        return tempCard;
    }

    public void setTempcard(String tempCard) {
        this.tempCard = tempCard;
    }
    public String getClickedcard() {
        return clickedCard;
    }

    public void setClickedcard(String clickedCard) {
        this.clickedCard = clickedCard;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getTemp() {
        return temp;
    }

    public void setTemp(String temp) {
        this.temp = temp;
    }
    public String getDestination() {
        return destination;
    }

    public void setDestination(String destination) {
        this.destination = destination;
    }


}