# Title: 

## Team Member(s):
(Note: Don't put your email addresses here (which is public).  If a student wants their NAME hidden as well, due to optional FERPA regulations, they can be listed purely by their GitHub ID).

# Monte Carlo Simulation Scenario & Purpose:

### Hypothesis before running the simulation:

* International terminal: 1
* Domestic terminal: 3
* Check-in counter in each terminal: 5

1. The average wait time of the international airport terminal would greater than the average wait time of the domestic airport terminal.
2. The average wait time during the weekend would be greater than the average wait time during the weekdays.
3. Average wait time of check-in would be between 10 and 15 minutes. 
4. the average wait time before holiday would be greater than the average wait time during or after holiday.
### Simulation's variables of uncertainty
* date_time:The number of passengers come to the airport during a certain date and time. The date is used to determine whether 
  today is in weekday or in weekend. And whether it is around the holiday(from two days before the holiday and two days after   the holiday). There are four time ranges in one day, 6am-12pm, 12pm-6pm,6pm-12am,12am-6am.
* domterminal1,domterminal2,domterminal3,intterminal: Which terminal(international or domestic) each passenger goes to. Each     passenger would be assigned to one airport terminal randomly.
* checkin_time: The check-in time for each passenger. This variable is also random for each passenger, the number would be       between 1s to 120s. 
* extra_checktime: Additional check-in time for those passengers bring liquid, and other things that cannot be taken on board.
  The system would pick up those passengers need extra check-in time randomly, the probability would between 1/500 and 1/10.
## Instructions on how to use the program:
After running this program, users would need to input their date and time of when they would arrive the airport.

## Sources Used:

