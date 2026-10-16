# Q001 — Draw.io Architecture Worksheet

[فارسی](drawio.fa.md) · [Overview](../README.md)

**You draw the diagram.** We deliberately do not supply a finished editable architecture. The question screenshot contains **text and answer options, not an architecture diagram**. When the learner contributes a genuine reference diagram, link it separately with source/permission noted.

## Manual drawing in https://app.diagrams.net

1. Choose **Device** (local save), then **Create New Diagram → Blank Diagram**. File name: `Q001-bicycle-location-api.drawio`.
2. Enable **More Shapes → AWS Architecture** if available; generic rectangles are fine. Do not spend the lab time hunting for icon assets.
3. From left to right draw a **Synthetic Bike Client** (outside AWS), an **AWS Cloud** boundary, **Amazon API Gateway HTTP API**, and **AWS Lambda**.
4. Draw **CloudWatch Log Group** below Lambda. Mark a dashed arrow **execution logs** from Lambda to CloudWatch (not a GPS data history pipeline).
5. Add `AWS_IAM / SigV4` on the **client → API** boundary. Add `IAM execution role` beside Lambda.
6. Add a solid arrow `POST /locations` to API Gateway, an arrow labeled `Lambda proxy integration v2.0`, and a return arrow labeled `HTTP 202 + accepted=true, stored=false`.
7. Put a distinct dashed empty box labeled `DynamoDB / location history — NOT IN THIS LAB`. Do not connect it as though deployed.
8. Add a side annotation: `Kinesis / Flink — optional stream processing in full architecture; NOT DEPLOYED`.
9. Use two styles: **solid = existing/tested when deployed**, **dashed = hypothetical/excluded**. Before any cloud run, label the solid resources as **planned**.
10. Export the image as `Q001-bicycle-location-api.png` or SVG; save the editable file locally, and add both to the kit's `diagrams/source/` and `diagrams/exported/` after reviewing privacy and correctness.

## Self-check

- [ ] I can explain why an API accepts a request but does not persist it.
- [ ] I can point to the caller IAM permission and Lambda execution role as **different** policies.
- [ ] I can identify the failure path for unsigned/invalid requests.
- [ ] I can explain how adding a datastore would change the diagram.
- [ ] I can redraw the diagram without looking at the worksheet.

**Portfolio prompt:** Under the diagram, explain in your own words what this micro-lab does *and does not* demonstrate.
