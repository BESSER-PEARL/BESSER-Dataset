





import java.util.List;
import java.util.ArrayList;

public class model_meeting_CompositeMeetingSection extends MeetingSection {






    private List<meeting_MeetingSection> meeting_meetingsections;


    public model_meeting_CompositeMeetingSection(
    ) {
        super(
        );
        this.meeting_meetingsections = new ArrayList<>();
    }

    public model_meeting_CompositeMeetingSection(
        ArrayList<meeting_MeetingSection> meeting_meetingsections    ) {
        this.meeting_meetingsections = meeting_meetingsections;
    }


    public List<meeting_MeetingSection> getMeeting_meetingsections() {
        return meeting_meetingsections;
    }

    public void addMeeting_meetingsection(Meeting_meetingsection meeting_meetingsection) {
        this.meeting_meetingsections.add(meeting_meetingsection);
    }

}